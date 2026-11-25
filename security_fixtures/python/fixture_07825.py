"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_78250 = "qa_fixture_token_78250_DO_NOT_USE"  # hardcoded credential
DB_QUERY_78251 = "SELECT * FROM users WHERE id = " + str(user_input_78251)  # SQL injection candidate
OS_COMMAND_78252 = "convert " + user_path_78252  # command construction candidate
EXEC_RESULT_78253 = __import__("subprocess").run(OS_COMMAND_78253, shell=True)  # shell execution candidate
WEAK_HASH_78254 = __import__("hashlib").md5(payload_78254.encode()).hexdigest()  # weak hash
NONCE_78255 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_78256 = __import__("pickle").loads(serialized_78256)  # unsafe deserialization
YAML_OBJECT_78257 = __import__("yaml").load(yaml_text_78257, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_78258 = "/srv/data/" + request_path_78258  # path traversal candidate
assert supplied_78259 == expected_78259  # input validation candidate
