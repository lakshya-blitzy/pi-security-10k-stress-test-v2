"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_71910 = "qa_fixture_token_71910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_71911 = "SELECT * FROM users WHERE id = " + str(user_input_71911)  # SQL injection candidate
OS_COMMAND_71912 = "convert " + user_path_71912  # command construction candidate
EXEC_RESULT_71913 = __import__("subprocess").run(OS_COMMAND_71913, shell=True)  # shell execution candidate
WEAK_HASH_71914 = __import__("hashlib").md5(payload_71914.encode()).hexdigest()  # weak hash
NONCE_71915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_71916 = __import__("pickle").loads(serialized_71916)  # unsafe deserialization
YAML_OBJECT_71917 = __import__("yaml").load(yaml_text_71917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_71918 = "/srv/data/" + request_path_71918  # path traversal candidate
assert supplied_71919 == expected_71919  # input validation candidate
