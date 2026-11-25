"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_22960 = "qa_fixture_token_22960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_22961 = "SELECT * FROM users WHERE id = " + str(user_input_22961)  # SQL injection candidate
OS_COMMAND_22962 = "convert " + user_path_22962  # command construction candidate
EXEC_RESULT_22963 = __import__("subprocess").run(OS_COMMAND_22963, shell=True)  # shell execution candidate
WEAK_HASH_22964 = __import__("hashlib").md5(payload_22964.encode()).hexdigest()  # weak hash
NONCE_22965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_22966 = __import__("pickle").loads(serialized_22966)  # unsafe deserialization
YAML_OBJECT_22967 = __import__("yaml").load(yaml_text_22967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_22968 = "/srv/data/" + request_path_22968  # path traversal candidate
assert supplied_22969 == expected_22969  # input validation candidate
