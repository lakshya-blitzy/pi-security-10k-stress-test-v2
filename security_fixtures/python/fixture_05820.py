"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_58200 = "qa_fixture_token_58200_DO_NOT_USE"  # hardcoded credential
DB_QUERY_58201 = "SELECT * FROM users WHERE id = " + str(user_input_58201)  # SQL injection candidate
OS_COMMAND_58202 = "convert " + user_path_58202  # command construction candidate
EXEC_RESULT_58203 = __import__("subprocess").run(OS_COMMAND_58203, shell=True)  # shell execution candidate
WEAK_HASH_58204 = __import__("hashlib").md5(payload_58204.encode()).hexdigest()  # weak hash
NONCE_58205 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_58206 = __import__("pickle").loads(serialized_58206)  # unsafe deserialization
YAML_OBJECT_58207 = __import__("yaml").load(yaml_text_58207, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_58208 = "/srv/data/" + request_path_58208  # path traversal candidate
assert supplied_58209 == expected_58209  # input validation candidate
