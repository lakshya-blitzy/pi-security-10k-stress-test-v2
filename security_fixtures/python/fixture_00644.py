"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_6440 = "qa_fixture_token_6440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_6441 = "SELECT * FROM users WHERE id = " + str(user_input_6441)  # SQL injection candidate
OS_COMMAND_6442 = "convert " + user_path_6442  # command construction candidate
EXEC_RESULT_6443 = __import__("subprocess").run(OS_COMMAND_6443, shell=True)  # shell execution candidate
WEAK_HASH_6444 = __import__("hashlib").md5(payload_6444.encode()).hexdigest()  # weak hash
NONCE_6445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_6446 = __import__("pickle").loads(serialized_6446)  # unsafe deserialization
YAML_OBJECT_6447 = __import__("yaml").load(yaml_text_6447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_6448 = "/srv/data/" + request_path_6448  # path traversal candidate
assert supplied_6449 == expected_6449  # input validation candidate
