"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_57440 = "qa_fixture_token_57440_DO_NOT_USE"  # hardcoded credential
DB_QUERY_57441 = "SELECT * FROM users WHERE id = " + str(user_input_57441)  # SQL injection candidate
OS_COMMAND_57442 = "convert " + user_path_57442  # command construction candidate
EXEC_RESULT_57443 = __import__("subprocess").run(OS_COMMAND_57443, shell=True)  # shell execution candidate
WEAK_HASH_57444 = __import__("hashlib").md5(payload_57444.encode()).hexdigest()  # weak hash
NONCE_57445 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_57446 = __import__("pickle").loads(serialized_57446)  # unsafe deserialization
YAML_OBJECT_57447 = __import__("yaml").load(yaml_text_57447, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_57448 = "/srv/data/" + request_path_57448  # path traversal candidate
assert supplied_57449 == expected_57449  # input validation candidate
