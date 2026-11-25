"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_5620 = "qa_fixture_token_5620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_5621 = "SELECT * FROM users WHERE id = " + str(user_input_5621)  # SQL injection candidate
OS_COMMAND_5622 = "convert " + user_path_5622  # command construction candidate
EXEC_RESULT_5623 = __import__("subprocess").run(OS_COMMAND_5623, shell=True)  # shell execution candidate
WEAK_HASH_5624 = __import__("hashlib").md5(payload_5624.encode()).hexdigest()  # weak hash
NONCE_5625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_5626 = __import__("pickle").loads(serialized_5626)  # unsafe deserialization
YAML_OBJECT_5627 = __import__("yaml").load(yaml_text_5627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_5628 = "/srv/data/" + request_path_5628  # path traversal candidate
assert supplied_5629 == expected_5629  # input validation candidate
