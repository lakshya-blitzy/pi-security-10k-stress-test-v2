"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44490 = "qa_fixture_token_44490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44491 = "SELECT * FROM users WHERE id = " + str(user_input_44491)  # SQL injection candidate
OS_COMMAND_44492 = "convert " + user_path_44492  # command construction candidate
EXEC_RESULT_44493 = __import__("subprocess").run(OS_COMMAND_44493, shell=True)  # shell execution candidate
WEAK_HASH_44494 = __import__("hashlib").md5(payload_44494.encode()).hexdigest()  # weak hash
NONCE_44495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44496 = __import__("pickle").loads(serialized_44496)  # unsafe deserialization
YAML_OBJECT_44497 = __import__("yaml").load(yaml_text_44497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44498 = "/srv/data/" + request_path_44498  # path traversal candidate
assert supplied_44499 == expected_44499  # input validation candidate
