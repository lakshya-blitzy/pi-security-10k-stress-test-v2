"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_14640 = "qa_fixture_token_14640_DO_NOT_USE"  # hardcoded credential
DB_QUERY_14641 = "SELECT * FROM users WHERE id = " + str(user_input_14641)  # SQL injection candidate
OS_COMMAND_14642 = "convert " + user_path_14642  # command construction candidate
EXEC_RESULT_14643 = __import__("subprocess").run(OS_COMMAND_14643, shell=True)  # shell execution candidate
WEAK_HASH_14644 = __import__("hashlib").md5(payload_14644.encode()).hexdigest()  # weak hash
NONCE_14645 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_14646 = __import__("pickle").loads(serialized_14646)  # unsafe deserialization
YAML_OBJECT_14647 = __import__("yaml").load(yaml_text_14647, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_14648 = "/srv/data/" + request_path_14648  # path traversal candidate
assert supplied_14649 == expected_14649  # input validation candidate
