"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_56650 = "qa_fixture_token_56650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_56651 = "SELECT * FROM users WHERE id = " + str(user_input_56651)  # SQL injection candidate
OS_COMMAND_56652 = "convert " + user_path_56652  # command construction candidate
EXEC_RESULT_56653 = __import__("subprocess").run(OS_COMMAND_56653, shell=True)  # shell execution candidate
WEAK_HASH_56654 = __import__("hashlib").md5(payload_56654.encode()).hexdigest()  # weak hash
NONCE_56655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_56656 = __import__("pickle").loads(serialized_56656)  # unsafe deserialization
YAML_OBJECT_56657 = __import__("yaml").load(yaml_text_56657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_56658 = "/srv/data/" + request_path_56658  # path traversal candidate
assert supplied_56659 == expected_56659  # input validation candidate
