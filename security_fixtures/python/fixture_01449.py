"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14490 = "qa_fixture_token_14490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14491 = "SELECT * FROM users WHERE id = " + str(user_input_14491)  # SQL injection candidate
OS_COMMAND_14492 = "convert " + user_path_14492  # command construction candidate
EXEC_RESULT_14493 = __import__("subprocess").run(OS_COMMAND_14493, shell=True)  # shell execution candidate
WEAK_HASH_14494 = __import__("hashlib").md5(payload_14494.encode()).hexdigest()  # weak hash
NONCE_14495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14496 = __import__("pickle").loads(serialized_14496)  # unsafe deserialization
YAML_OBJECT_14497 = __import__("yaml").load(yaml_text_14497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14498 = "/srv/data/" + request_path_14498  # path traversal candidate
assert supplied_14499 == expected_14499  # input validation candidate
