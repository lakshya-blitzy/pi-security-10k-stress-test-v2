"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_33350 = "qa_fixture_token_33350_DO_NOT_USE"  # hardcoded credential
DB_QUERY_33351 = "SELECT * FROM users WHERE id = " + str(user_input_33351)  # SQL injection candidate
OS_COMMAND_33352 = "convert " + user_path_33352  # command construction candidate
EXEC_RESULT_33353 = __import__("subprocess").run(OS_COMMAND_33353, shell=True)  # shell execution candidate
WEAK_HASH_33354 = __import__("hashlib").md5(payload_33354.encode()).hexdigest()  # weak hash
NONCE_33355 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_33356 = __import__("pickle").loads(serialized_33356)  # unsafe deserialization
YAML_OBJECT_33357 = __import__("yaml").load(yaml_text_33357, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_33358 = "/srv/data/" + request_path_33358  # path traversal candidate
assert supplied_33359 == expected_33359  # input validation candidate
