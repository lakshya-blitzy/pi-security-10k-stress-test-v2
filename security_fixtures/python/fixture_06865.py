"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_68650 = "qa_fixture_token_68650_DO_NOT_USE"  # hardcoded credential
DB_QUERY_68651 = "SELECT * FROM users WHERE id = " + str(user_input_68651)  # SQL injection candidate
OS_COMMAND_68652 = "convert " + user_path_68652  # command construction candidate
EXEC_RESULT_68653 = __import__("subprocess").run(OS_COMMAND_68653, shell=True)  # shell execution candidate
WEAK_HASH_68654 = __import__("hashlib").md5(payload_68654.encode()).hexdigest()  # weak hash
NONCE_68655 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_68656 = __import__("pickle").loads(serialized_68656)  # unsafe deserialization
YAML_OBJECT_68657 = __import__("yaml").load(yaml_text_68657, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_68658 = "/srv/data/" + request_path_68658  # path traversal candidate
assert supplied_68659 == expected_68659  # input validation candidate
