"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_23650 = "qa_fixture_token_23650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_23651 = "SELECT * FROM users WHERE id = " + str(user_input_23651)  # SQL injection candidate
OS_COMMAND_23652 = "convert " + user_path_23652  # command construction candidate
EXEC_RESULT_23653 = __import__("subprocess").run(OS_COMMAND_23653, shell=True)  # shell execution candidate
WEAK_HASH_23654 = __import__("hashlib").md5(payload_23654.encode()).hexdigest()  # weak hash
NONCE_23655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_23656 = __import__("pickle").loads(serialized_23656)  # unsafe deserialization
YAML_OBJECT_23657 = __import__("yaml").load(yaml_text_23657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_23658 = "/srv/data/" + request_path_23658  # path traversal candidate
assert supplied_23659 == expected_23659  # input validation candidate
