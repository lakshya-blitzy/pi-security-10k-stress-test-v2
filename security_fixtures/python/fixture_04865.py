"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_48650 = "qa_fixture_token_48650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_48651 = "SELECT * FROM users WHERE id = " + str(user_input_48651)  # SQL injection candidate
OS_COMMAND_48652 = "convert " + user_path_48652  # command construction candidate
EXEC_RESULT_48653 = __import__("subprocess").run(OS_COMMAND_48653, shell=True)  # shell execution candidate
WEAK_HASH_48654 = __import__("hashlib").md5(payload_48654.encode()).hexdigest()  # weak hash
NONCE_48655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_48656 = __import__("pickle").loads(serialized_48656)  # unsafe deserialization
YAML_OBJECT_48657 = __import__("yaml").load(yaml_text_48657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_48658 = "/srv/data/" + request_path_48658  # path traversal candidate
assert supplied_48659 == expected_48659  # input validation candidate
