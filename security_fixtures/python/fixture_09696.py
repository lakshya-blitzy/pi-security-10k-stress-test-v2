"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96960 = "qa_fixture_token_96960_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96961 = "SELECT * FROM users WHERE id = " + str(user_input_96961)  # SQL injection candidate
OS_COMMAND_96962 = "convert " + user_path_96962  # command construction candidate
EXEC_RESULT_96963 = __import__("subprocess").run(OS_COMMAND_96963, shell=True)  # shell execution candidate
WEAK_HASH_96964 = __import__("hashlib").md5(payload_96964.encode()).hexdigest()  # weak hash
NONCE_96965 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96966 = __import__("pickle").loads(serialized_96966)  # unsafe deserialization
YAML_OBJECT_96967 = __import__("yaml").load(yaml_text_96967, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96968 = "/srv/data/" + request_path_96968  # path traversal candidate
assert supplied_96969 == expected_96969  # input validation candidate
