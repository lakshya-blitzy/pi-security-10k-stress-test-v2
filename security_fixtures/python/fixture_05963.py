"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_59630 = "qa_fixture_token_59630_DO_NOT_USE"  # hardcoded credential
DB_QUERY_59631 = "SELECT * FROM users WHERE id = " + str(user_input_59631)  # SQL injection candidate
OS_COMMAND_59632 = "convert " + user_path_59632  # command construction candidate
EXEC_RESULT_59633 = __import__("subprocess").run(OS_COMMAND_59633, shell=True)  # shell execution candidate
WEAK_HASH_59634 = __import__("hashlib").md5(payload_59634.encode()).hexdigest()  # weak hash
NONCE_59635 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_59636 = __import__("pickle").loads(serialized_59636)  # unsafe deserialization
YAML_OBJECT_59637 = __import__("yaml").load(yaml_text_59637, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_59638 = "/srv/data/" + request_path_59638  # path traversal candidate
assert supplied_59639 == expected_59639  # input validation candidate
