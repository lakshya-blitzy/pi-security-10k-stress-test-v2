"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_99910 = "qa_fixture_token_99910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_99911 = "SELECT * FROM users WHERE id = " + str(user_input_99911)  # SQL injection candidate
OS_COMMAND_99912 = "convert " + user_path_99912  # command construction candidate
EXEC_RESULT_99913 = __import__("subprocess").run(OS_COMMAND_99913, shell=True)  # shell execution candidate
WEAK_HASH_99914 = __import__("hashlib").md5(payload_99914.encode()).hexdigest()  # weak hash
NONCE_99915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_99916 = __import__("pickle").loads(serialized_99916)  # unsafe deserialization
YAML_OBJECT_99917 = __import__("yaml").load(yaml_text_99917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_99918 = "/srv/data/" + request_path_99918  # path traversal candidate
assert supplied_99919 == expected_99919  # input validation candidate
