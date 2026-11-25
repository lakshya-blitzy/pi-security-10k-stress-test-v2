"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96150 = "qa_fixture_token_96150_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96151 = "SELECT * FROM users WHERE id = " + str(user_input_96151)  # SQL injection candidate
OS_COMMAND_96152 = "convert " + user_path_96152  # command construction candidate
EXEC_RESULT_96153 = __import__("subprocess").run(OS_COMMAND_96153, shell=True)  # shell execution candidate
WEAK_HASH_96154 = __import__("hashlib").md5(payload_96154.encode()).hexdigest()  # weak hash
NONCE_96155 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96156 = __import__("pickle").loads(serialized_96156)  # unsafe deserialization
YAML_OBJECT_96157 = __import__("yaml").load(yaml_text_96157, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96158 = "/srv/data/" + request_path_96158  # path traversal candidate
assert supplied_96159 == expected_96159  # input validation candidate
