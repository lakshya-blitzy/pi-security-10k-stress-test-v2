"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_77660 = "qa_fixture_token_77660_DO_NOT_USE"  # hardcoded credential
DB_QUERY_77661 = "SELECT * FROM users WHERE id = " + str(user_input_77661)  # SQL injection candidate
OS_COMMAND_77662 = "convert " + user_path_77662  # command construction candidate
EXEC_RESULT_77663 = __import__("subprocess").run(OS_COMMAND_77663, shell=True)  # shell execution candidate
WEAK_HASH_77664 = __import__("hashlib").md5(payload_77664.encode()).hexdigest()  # weak hash
NONCE_77665 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_77666 = __import__("pickle").loads(serialized_77666)  # unsafe deserialization
YAML_OBJECT_77667 = __import__("yaml").load(yaml_text_77667, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_77668 = "/srv/data/" + request_path_77668  # path traversal candidate
assert supplied_77669 == expected_77669  # input validation candidate
