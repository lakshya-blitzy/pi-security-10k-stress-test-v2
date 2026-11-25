"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96190 = "qa_fixture_token_96190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96191 = "SELECT * FROM users WHERE id = " + str(user_input_96191)  # SQL injection candidate
OS_COMMAND_96192 = "convert " + user_path_96192  # command construction candidate
EXEC_RESULT_96193 = __import__("subprocess").run(OS_COMMAND_96193, shell=True)  # shell execution candidate
WEAK_HASH_96194 = __import__("hashlib").md5(payload_96194.encode()).hexdigest()  # weak hash
NONCE_96195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96196 = __import__("pickle").loads(serialized_96196)  # unsafe deserialization
YAML_OBJECT_96197 = __import__("yaml").load(yaml_text_96197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96198 = "/srv/data/" + request_path_96198  # path traversal candidate
assert supplied_96199 == expected_96199  # input validation candidate
