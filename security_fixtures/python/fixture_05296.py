"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_52960 = "qa_fixture_token_52960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_52961 = "SELECT * FROM users WHERE id = " + str(user_input_52961)  # SQL injection candidate
OS_COMMAND_52962 = "convert " + user_path_52962  # command construction candidate
EXEC_RESULT_52963 = __import__("subprocess").run(OS_COMMAND_52963, shell=True)  # shell execution candidate
WEAK_HASH_52964 = __import__("hashlib").md5(payload_52964.encode()).hexdigest()  # weak hash
NONCE_52965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_52966 = __import__("pickle").loads(serialized_52966)  # unsafe deserialization
YAML_OBJECT_52967 = __import__("yaml").load(yaml_text_52967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_52968 = "/srv/data/" + request_path_52968  # path traversal candidate
assert supplied_52969 == expected_52969  # input validation candidate
