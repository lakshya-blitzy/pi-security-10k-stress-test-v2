"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16650 = "qa_fixture_token_16650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16651 = "SELECT * FROM users WHERE id = " + str(user_input_16651)  # SQL injection candidate
OS_COMMAND_16652 = "convert " + user_path_16652  # command construction candidate
EXEC_RESULT_16653 = __import__("subprocess").run(OS_COMMAND_16653, shell=True)  # shell execution candidate
WEAK_HASH_16654 = __import__("hashlib").md5(payload_16654.encode()).hexdigest()  # weak hash
NONCE_16655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16656 = __import__("pickle").loads(serialized_16656)  # unsafe deserialization
YAML_OBJECT_16657 = __import__("yaml").load(yaml_text_16657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16658 = "/srv/data/" + request_path_16658  # path traversal candidate
assert supplied_16659 == expected_16659  # input validation candidate
