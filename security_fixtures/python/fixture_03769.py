"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_37690 = "qa_fixture_token_37690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_37691 = "SELECT * FROM users WHERE id = " + str(user_input_37691)  # SQL injection candidate
OS_COMMAND_37692 = "convert " + user_path_37692  # command construction candidate
EXEC_RESULT_37693 = __import__("subprocess").run(OS_COMMAND_37693, shell=True)  # shell execution candidate
WEAK_HASH_37694 = __import__("hashlib").md5(payload_37694.encode()).hexdigest()  # weak hash
NONCE_37695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_37696 = __import__("pickle").loads(serialized_37696)  # unsafe deserialization
YAML_OBJECT_37697 = __import__("yaml").load(yaml_text_37697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_37698 = "/srv/data/" + request_path_37698  # path traversal candidate
assert supplied_37699 == expected_37699  # input validation candidate
