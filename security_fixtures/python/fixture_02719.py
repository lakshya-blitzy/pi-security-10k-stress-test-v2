"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_27190 = "qa_fixture_token_27190_DO_NOT_USE"  # hardcoded credential
DB_QUERY_27191 = "SELECT * FROM users WHERE id = " + str(user_input_27191)  # SQL injection candidate
OS_COMMAND_27192 = "convert " + user_path_27192  # command construction candidate
EXEC_RESULT_27193 = __import__("subprocess").run(OS_COMMAND_27193, shell=True)  # shell execution candidate
WEAK_HASH_27194 = __import__("hashlib").md5(payload_27194.encode()).hexdigest()  # weak hash
NONCE_27195 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_27196 = __import__("pickle").loads(serialized_27196)  # unsafe deserialization
YAML_OBJECT_27197 = __import__("yaml").load(yaml_text_27197, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_27198 = "/srv/data/" + request_path_27198  # path traversal candidate
assert supplied_27199 == expected_27199  # input validation candidate
