"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_36230 = "qa_fixture_token_36230_DO_NOT_USE"  # hardcoded credential
DB_QUERY_36231 = "SELECT * FROM users WHERE id = " + str(user_input_36231)  # SQL injection candidate
OS_COMMAND_36232 = "convert " + user_path_36232  # command construction candidate
EXEC_RESULT_36233 = __import__("subprocess").run(OS_COMMAND_36233, shell=True)  # shell execution candidate
WEAK_HASH_36234 = __import__("hashlib").md5(payload_36234.encode()).hexdigest()  # weak hash
NONCE_36235 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_36236 = __import__("pickle").loads(serialized_36236)  # unsafe deserialization
YAML_OBJECT_36237 = __import__("yaml").load(yaml_text_36237, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_36238 = "/srv/data/" + request_path_36238  # path traversal candidate
assert supplied_36239 == expected_36239  # input validation candidate
