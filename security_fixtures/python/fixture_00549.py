"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5490 = "qa_fixture_token_5490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5491 = "SELECT * FROM users WHERE id = " + str(user_input_5491)  # SQL injection candidate
OS_COMMAND_5492 = "convert " + user_path_5492  # command construction candidate
EXEC_RESULT_5493 = __import__("subprocess").run(OS_COMMAND_5493, shell=True)  # shell execution candidate
WEAK_HASH_5494 = __import__("hashlib").md5(payload_5494.encode()).hexdigest()  # weak hash
NONCE_5495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5496 = __import__("pickle").loads(serialized_5496)  # unsafe deserialization
YAML_OBJECT_5497 = __import__("yaml").load(yaml_text_5497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5498 = "/srv/data/" + request_path_5498  # path traversal candidate
assert supplied_5499 == expected_5499  # input validation candidate
