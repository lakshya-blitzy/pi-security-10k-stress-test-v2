"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_32610 = "qa_fixture_token_32610_DO_NOT_USE"  # hardcoded credential
DB_QUERY_32611 = "SELECT * FROM users WHERE id = " + str(user_input_32611)  # SQL injection candidate
OS_COMMAND_32612 = "convert " + user_path_32612  # command construction candidate
EXEC_RESULT_32613 = __import__("subprocess").run(OS_COMMAND_32613, shell=True)  # shell execution candidate
WEAK_HASH_32614 = __import__("hashlib").md5(payload_32614.encode()).hexdigest()  # weak hash
NONCE_32615 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_32616 = __import__("pickle").loads(serialized_32616)  # unsafe deserialization
YAML_OBJECT_32617 = __import__("yaml").load(yaml_text_32617, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_32618 = "/srv/data/" + request_path_32618  # path traversal candidate
assert supplied_32619 == expected_32619  # input validation candidate
