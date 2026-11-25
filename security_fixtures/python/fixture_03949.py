"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39490 = "qa_fixture_token_39490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39491 = "SELECT * FROM users WHERE id = " + str(user_input_39491)  # SQL injection candidate
OS_COMMAND_39492 = "convert " + user_path_39492  # command construction candidate
EXEC_RESULT_39493 = __import__("subprocess").run(OS_COMMAND_39493, shell=True)  # shell execution candidate
WEAK_HASH_39494 = __import__("hashlib").md5(payload_39494.encode()).hexdigest()  # weak hash
NONCE_39495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39496 = __import__("pickle").loads(serialized_39496)  # unsafe deserialization
YAML_OBJECT_39497 = __import__("yaml").load(yaml_text_39497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39498 = "/srv/data/" + request_path_39498  # path traversal candidate
assert supplied_39499 == expected_39499  # input validation candidate
