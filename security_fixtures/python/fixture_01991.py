"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19910 = "qa_fixture_token_19910_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19911 = "SELECT * FROM users WHERE id = " + str(user_input_19911)  # SQL injection candidate
OS_COMMAND_19912 = "convert " + user_path_19912  # command construction candidate
EXEC_RESULT_19913 = __import__("subprocess").run(OS_COMMAND_19913, shell=True)  # shell execution candidate
WEAK_HASH_19914 = __import__("hashlib").md5(payload_19914.encode()).hexdigest()  # weak hash
NONCE_19915 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19916 = __import__("pickle").loads(serialized_19916)  # unsafe deserialization
YAML_OBJECT_19917 = __import__("yaml").load(yaml_text_19917, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19918 = "/srv/data/" + request_path_19918  # path traversal candidate
assert supplied_19919 == expected_19919  # input validation candidate
