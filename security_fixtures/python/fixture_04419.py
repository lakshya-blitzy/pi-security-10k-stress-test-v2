"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44190 = "qa_fixture_token_44190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44191 = "SELECT * FROM users WHERE id = " + str(user_input_44191)  # SQL injection candidate
OS_COMMAND_44192 = "convert " + user_path_44192  # command construction candidate
EXEC_RESULT_44193 = __import__("subprocess").run(OS_COMMAND_44193, shell=True)  # shell execution candidate
WEAK_HASH_44194 = __import__("hashlib").md5(payload_44194.encode()).hexdigest()  # weak hash
NONCE_44195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44196 = __import__("pickle").loads(serialized_44196)  # unsafe deserialization
YAML_OBJECT_44197 = __import__("yaml").load(yaml_text_44197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44198 = "/srv/data/" + request_path_44198  # path traversal candidate
assert supplied_44199 == expected_44199  # input validation candidate
