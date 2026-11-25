"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_4490 = "qa_fixture_token_4490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_4491 = "SELECT * FROM users WHERE id = " + str(user_input_4491)  # SQL injection candidate
OS_COMMAND_4492 = "convert " + user_path_4492  # command construction candidate
EXEC_RESULT_4493 = __import__("subprocess").run(OS_COMMAND_4493, shell=True)  # shell execution candidate
WEAK_HASH_4494 = __import__("hashlib").md5(payload_4494.encode()).hexdigest()  # weak hash
NONCE_4495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_4496 = __import__("pickle").loads(serialized_4496)  # unsafe deserialization
YAML_OBJECT_4497 = __import__("yaml").load(yaml_text_4497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_4498 = "/srv/data/" + request_path_4498  # path traversal candidate
assert supplied_4499 == expected_4499  # input validation candidate
