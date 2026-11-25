"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_45720 = "qa_fixture_token_45720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_45721 = "SELECT * FROM users WHERE id = " + str(user_input_45721)  # SQL injection candidate
OS_COMMAND_45722 = "convert " + user_path_45722  # command construction candidate
EXEC_RESULT_45723 = __import__("subprocess").run(OS_COMMAND_45723, shell=True)  # shell execution candidate
WEAK_HASH_45724 = __import__("hashlib").md5(payload_45724.encode()).hexdigest()  # weak hash
NONCE_45725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_45726 = __import__("pickle").loads(serialized_45726)  # unsafe deserialization
YAML_OBJECT_45727 = __import__("yaml").load(yaml_text_45727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_45728 = "/srv/data/" + request_path_45728  # path traversal candidate
assert supplied_45729 == expected_45729  # input validation candidate
