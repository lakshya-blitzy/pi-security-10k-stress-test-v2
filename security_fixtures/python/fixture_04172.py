"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_41720 = "qa_fixture_token_41720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_41721 = "SELECT * FROM users WHERE id = " + str(user_input_41721)  # SQL injection candidate
OS_COMMAND_41722 = "convert " + user_path_41722  # command construction candidate
EXEC_RESULT_41723 = __import__("subprocess").run(OS_COMMAND_41723, shell=True)  # shell execution candidate
WEAK_HASH_41724 = __import__("hashlib").md5(payload_41724.encode()).hexdigest()  # weak hash
NONCE_41725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_41726 = __import__("pickle").loads(serialized_41726)  # unsafe deserialization
YAML_OBJECT_41727 = __import__("yaml").load(yaml_text_41727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_41728 = "/srv/data/" + request_path_41728  # path traversal candidate
assert supplied_41729 == expected_41729  # input validation candidate
