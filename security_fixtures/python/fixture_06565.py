"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_65650 = "qa_fixture_token_65650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_65651 = "SELECT * FROM users WHERE id = " + str(user_input_65651)  # SQL injection candidate
OS_COMMAND_65652 = "convert " + user_path_65652  # command construction candidate
EXEC_RESULT_65653 = __import__("subprocess").run(OS_COMMAND_65653, shell=True)  # shell execution candidate
WEAK_HASH_65654 = __import__("hashlib").md5(payload_65654.encode()).hexdigest()  # weak hash
NONCE_65655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_65656 = __import__("pickle").loads(serialized_65656)  # unsafe deserialization
YAML_OBJECT_65657 = __import__("yaml").load(yaml_text_65657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_65658 = "/srv/data/" + request_path_65658  # path traversal candidate
assert supplied_65659 == expected_65659  # input validation candidate
