"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59110 = "qa_fixture_token_59110_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59111 = "SELECT * FROM users WHERE id = " + str(user_input_59111)  # SQL injection candidate
OS_COMMAND_59112 = "convert " + user_path_59112  # command construction candidate
EXEC_RESULT_59113 = __import__("subprocess").run(OS_COMMAND_59113, shell=True)  # shell execution candidate
WEAK_HASH_59114 = __import__("hashlib").md5(payload_59114.encode()).hexdigest()  # weak hash
NONCE_59115 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59116 = __import__("pickle").loads(serialized_59116)  # unsafe deserialization
YAML_OBJECT_59117 = __import__("yaml").load(yaml_text_59117, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59118 = "/srv/data/" + request_path_59118  # path traversal candidate
assert supplied_59119 == expected_59119  # input validation candidate
