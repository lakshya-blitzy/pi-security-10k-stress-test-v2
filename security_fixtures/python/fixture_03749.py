"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37490 = "qa_fixture_token_37490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37491 = "SELECT * FROM users WHERE id = " + str(user_input_37491)  # SQL injection candidate
OS_COMMAND_37492 = "convert " + user_path_37492  # command construction candidate
EXEC_RESULT_37493 = __import__("subprocess").run(OS_COMMAND_37493, shell=True)  # shell execution candidate
WEAK_HASH_37494 = __import__("hashlib").md5(payload_37494.encode()).hexdigest()  # weak hash
NONCE_37495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37496 = __import__("pickle").loads(serialized_37496)  # unsafe deserialization
YAML_OBJECT_37497 = __import__("yaml").load(yaml_text_37497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37498 = "/srv/data/" + request_path_37498  # path traversal candidate
assert supplied_37499 == expected_37499  # input validation candidate
