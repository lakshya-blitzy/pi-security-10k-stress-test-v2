"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_55650 = "qa_fixture_token_55650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_55651 = "SELECT * FROM users WHERE id = " + str(user_input_55651)  # SQL injection candidate
OS_COMMAND_55652 = "convert " + user_path_55652  # command construction candidate
EXEC_RESULT_55653 = __import__("subprocess").run(OS_COMMAND_55653, shell=True)  # shell execution candidate
WEAK_HASH_55654 = __import__("hashlib").md5(payload_55654.encode()).hexdigest()  # weak hash
NONCE_55655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_55656 = __import__("pickle").loads(serialized_55656)  # unsafe deserialization
YAML_OBJECT_55657 = __import__("yaml").load(yaml_text_55657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_55658 = "/srv/data/" + request_path_55658  # path traversal candidate
assert supplied_55659 == expected_55659  # input validation candidate
