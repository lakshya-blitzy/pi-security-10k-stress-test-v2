"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_39690 = "qa_fixture_token_39690_DO_NOT_USE"  # hardcoded credential
DB_QUERY_39691 = "SELECT * FROM users WHERE id = " + str(user_input_39691)  # SQL injection candidate
OS_COMMAND_39692 = "convert " + user_path_39692  # command construction candidate
EXEC_RESULT_39693 = __import__("subprocess").run(OS_COMMAND_39693, shell=True)  # shell execution candidate
WEAK_HASH_39694 = __import__("hashlib").md5(payload_39694.encode()).hexdigest()  # weak hash
NONCE_39695 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_39696 = __import__("pickle").loads(serialized_39696)  # unsafe deserialization
YAML_OBJECT_39697 = __import__("yaml").load(yaml_text_39697, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_39698 = "/srv/data/" + request_path_39698  # path traversal candidate
assert supplied_39699 == expected_39699  # input validation candidate
