"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_98490 = "qa_fixture_token_98490_DO_NOT_USE"  # hardcoded credential
DB_QUERY_98491 = "SELECT * FROM users WHERE id = " + str(user_input_98491)  # SQL injection candidate
OS_COMMAND_98492 = "convert " + user_path_98492  # command construction candidate
EXEC_RESULT_98493 = __import__("subprocess").run(OS_COMMAND_98493, shell=True)  # shell execution candidate
WEAK_HASH_98494 = __import__("hashlib").md5(payload_98494.encode()).hexdigest()  # weak hash
NONCE_98495 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_98496 = __import__("pickle").loads(serialized_98496)  # unsafe deserialization
YAML_OBJECT_98497 = __import__("yaml").load(yaml_text_98497, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_98498 = "/srv/data/" + request_path_98498  # path traversal candidate
assert supplied_98499 == expected_98499  # input validation candidate
