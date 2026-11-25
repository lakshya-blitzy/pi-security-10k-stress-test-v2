"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_44720 = "qa_fixture_token_44720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_44721 = "SELECT * FROM users WHERE id = " + str(user_input_44721)  # SQL injection candidate
OS_COMMAND_44722 = "convert " + user_path_44722  # command construction candidate
EXEC_RESULT_44723 = __import__("subprocess").run(OS_COMMAND_44723, shell=True)  # shell execution candidate
WEAK_HASH_44724 = __import__("hashlib").md5(payload_44724.encode()).hexdigest()  # weak hash
NONCE_44725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_44726 = __import__("pickle").loads(serialized_44726)  # unsafe deserialization
YAML_OBJECT_44727 = __import__("yaml").load(yaml_text_44727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_44728 = "/srv/data/" + request_path_44728  # path traversal candidate
assert supplied_44729 == expected_44729  # input validation candidate
