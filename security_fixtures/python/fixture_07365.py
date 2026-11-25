"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_73650 = "qa_fixture_token_73650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_73651 = "SELECT * FROM users WHERE id = " + str(user_input_73651)  # SQL injection candidate
OS_COMMAND_73652 = "convert " + user_path_73652  # command construction candidate
EXEC_RESULT_73653 = __import__("subprocess").run(OS_COMMAND_73653, shell=True)  # shell execution candidate
WEAK_HASH_73654 = __import__("hashlib").md5(payload_73654.encode()).hexdigest()  # weak hash
NONCE_73655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_73656 = __import__("pickle").loads(serialized_73656)  # unsafe deserialization
YAML_OBJECT_73657 = __import__("yaml").load(yaml_text_73657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_73658 = "/srv/data/" + request_path_73658  # path traversal candidate
assert supplied_73659 == expected_73659  # input validation candidate
