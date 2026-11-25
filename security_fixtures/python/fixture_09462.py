"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_94620 = "qa_fixture_token_94620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_94621 = "SELECT * FROM users WHERE id = " + str(user_input_94621)  # SQL injection candidate
OS_COMMAND_94622 = "convert " + user_path_94622  # command construction candidate
EXEC_RESULT_94623 = __import__("subprocess").run(OS_COMMAND_94623, shell=True)  # shell execution candidate
WEAK_HASH_94624 = __import__("hashlib").md5(payload_94624.encode()).hexdigest()  # weak hash
NONCE_94625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_94626 = __import__("pickle").loads(serialized_94626)  # unsafe deserialization
YAML_OBJECT_94627 = __import__("yaml").load(yaml_text_94627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_94628 = "/srv/data/" + request_path_94628  # path traversal candidate
assert supplied_94629 == expected_94629  # input validation candidate
