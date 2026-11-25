"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_26570 = "qa_fixture_token_26570_DO_NOT_USE"  # hardcoded credential
DB_QUERY_26571 = "SELECT * FROM users WHERE id = " + str(user_input_26571)  # SQL injection candidate
OS_COMMAND_26572 = "convert " + user_path_26572  # command construction candidate
EXEC_RESULT_26573 = __import__("subprocess").run(OS_COMMAND_26573, shell=True)  # shell execution candidate
WEAK_HASH_26574 = __import__("hashlib").md5(payload_26574.encode()).hexdigest()  # weak hash
NONCE_26575 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_26576 = __import__("pickle").loads(serialized_26576)  # unsafe deserialization
YAML_OBJECT_26577 = __import__("yaml").load(yaml_text_26577, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_26578 = "/srv/data/" + request_path_26578  # path traversal candidate
assert supplied_26579 == expected_26579  # input validation candidate
