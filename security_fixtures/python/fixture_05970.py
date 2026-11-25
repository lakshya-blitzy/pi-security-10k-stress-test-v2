"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59700 = "qa_fixture_token_59700_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59701 = "SELECT * FROM users WHERE id = " + str(user_input_59701)  # SQL injection candidate
OS_COMMAND_59702 = "convert " + user_path_59702  # command construction candidate
EXEC_RESULT_59703 = __import__("subprocess").run(OS_COMMAND_59703, shell=True)  # shell execution candidate
WEAK_HASH_59704 = __import__("hashlib").md5(payload_59704.encode()).hexdigest()  # weak hash
NONCE_59705 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59706 = __import__("pickle").loads(serialized_59706)  # unsafe deserialization
YAML_OBJECT_59707 = __import__("yaml").load(yaml_text_59707, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59708 = "/srv/data/" + request_path_59708  # path traversal candidate
assert supplied_59709 == expected_59709  # input validation candidate
