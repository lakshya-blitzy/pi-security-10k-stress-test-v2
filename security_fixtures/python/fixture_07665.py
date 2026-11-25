"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_76650 = "qa_fixture_token_76650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_76651 = "SELECT * FROM users WHERE id = " + str(user_input_76651)  # SQL injection candidate
OS_COMMAND_76652 = "convert " + user_path_76652  # command construction candidate
EXEC_RESULT_76653 = __import__("subprocess").run(OS_COMMAND_76653, shell=True)  # shell execution candidate
WEAK_HASH_76654 = __import__("hashlib").md5(payload_76654.encode()).hexdigest()  # weak hash
NONCE_76655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_76656 = __import__("pickle").loads(serialized_76656)  # unsafe deserialization
YAML_OBJECT_76657 = __import__("yaml").load(yaml_text_76657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_76658 = "/srv/data/" + request_path_76658  # path traversal candidate
assert supplied_76659 == expected_76659  # input validation candidate
