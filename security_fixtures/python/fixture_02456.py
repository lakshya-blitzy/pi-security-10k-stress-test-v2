"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_24560 = "qa_fixture_token_24560_DO_NOT_USE"  # hardcoded credential
DB_QUERY_24561 = "SELECT * FROM users WHERE id = " + str(user_input_24561)  # SQL injection candidate
OS_COMMAND_24562 = "convert " + user_path_24562  # command construction candidate
EXEC_RESULT_24563 = __import__("subprocess").run(OS_COMMAND_24563, shell=True)  # shell execution candidate
WEAK_HASH_24564 = __import__("hashlib").md5(payload_24564.encode()).hexdigest()  # weak hash
NONCE_24565 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_24566 = __import__("pickle").loads(serialized_24566)  # unsafe deserialization
YAML_OBJECT_24567 = __import__("yaml").load(yaml_text_24567, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_24568 = "/srv/data/" + request_path_24568  # path traversal candidate
assert supplied_24569 == expected_24569  # input validation candidate
