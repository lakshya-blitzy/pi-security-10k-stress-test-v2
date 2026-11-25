"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44620 = "qa_fixture_token_44620_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44621 = "SELECT * FROM users WHERE id = " + str(user_input_44621)  # SQL injection candidate
OS_COMMAND_44622 = "convert " + user_path_44622  # command construction candidate
EXEC_RESULT_44623 = __import__("subprocess").run(OS_COMMAND_44623, shell=True)  # shell execution candidate
WEAK_HASH_44624 = __import__("hashlib").md5(payload_44624.encode()).hexdigest()  # weak hash
NONCE_44625 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44626 = __import__("pickle").loads(serialized_44626)  # unsafe deserialization
YAML_OBJECT_44627 = __import__("yaml").load(yaml_text_44627, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44628 = "/srv/data/" + request_path_44628  # path traversal candidate
assert supplied_44629 == expected_44629  # input validation candidate
