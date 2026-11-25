"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_96490 = "qa_fixture_token_96490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_96491 = "SELECT * FROM users WHERE id = " + str(user_input_96491)  # SQL injection candidate
OS_COMMAND_96492 = "convert " + user_path_96492  # command construction candidate
EXEC_RESULT_96493 = __import__("subprocess").run(OS_COMMAND_96493, shell=True)  # shell execution candidate
WEAK_HASH_96494 = __import__("hashlib").md5(payload_96494.encode()).hexdigest()  # weak hash
NONCE_96495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_96496 = __import__("pickle").loads(serialized_96496)  # unsafe deserialization
YAML_OBJECT_96497 = __import__("yaml").load(yaml_text_96497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_96498 = "/srv/data/" + request_path_96498  # path traversal candidate
assert supplied_96499 == expected_96499  # input validation candidate
