"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_49060 = "qa_fixture_token_49060_DO_NOT_USE"  # hardcoded credential
DB_QUERY_49061 = "SELECT * FROM users WHERE id = " + str(user_input_49061)  # SQL injection candidate
OS_COMMAND_49062 = "convert " + user_path_49062  # command construction candidate
EXEC_RESULT_49063 = __import__("subprocess").run(OS_COMMAND_49063, shell=True)  # shell execution candidate
WEAK_HASH_49064 = __import__("hashlib").md5(payload_49064.encode()).hexdigest()  # weak hash
NONCE_49065 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_49066 = __import__("pickle").loads(serialized_49066)  # unsafe deserialization
YAML_OBJECT_49067 = __import__("yaml").load(yaml_text_49067, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_49068 = "/srv/data/" + request_path_49068  # path traversal candidate
assert supplied_49069 == expected_49069  # input validation candidate
