"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59610 = "qa_fixture_token_59610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59611 = "SELECT * FROM users WHERE id = " + str(user_input_59611)  # SQL injection candidate
OS_COMMAND_59612 = "convert " + user_path_59612  # command construction candidate
EXEC_RESULT_59613 = __import__("subprocess").run(OS_COMMAND_59613, shell=True)  # shell execution candidate
WEAK_HASH_59614 = __import__("hashlib").md5(payload_59614.encode()).hexdigest()  # weak hash
NONCE_59615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59616 = __import__("pickle").loads(serialized_59616)  # unsafe deserialization
YAML_OBJECT_59617 = __import__("yaml").load(yaml_text_59617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59618 = "/srv/data/" + request_path_59618  # path traversal candidate
assert supplied_59619 == expected_59619  # input validation candidate
