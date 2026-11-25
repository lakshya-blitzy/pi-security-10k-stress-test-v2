"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_30830 = "qa_fixture_token_30830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_30831 = "SELECT * FROM users WHERE id = " + str(user_input_30831)  # SQL injection candidate
OS_COMMAND_30832 = "convert " + user_path_30832  # command construction candidate
EXEC_RESULT_30833 = __import__("subprocess").run(OS_COMMAND_30833, shell=True)  # shell execution candidate
WEAK_HASH_30834 = __import__("hashlib").md5(payload_30834.encode()).hexdigest()  # weak hash
NONCE_30835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_30836 = __import__("pickle").loads(serialized_30836)  # unsafe deserialization
YAML_OBJECT_30837 = __import__("yaml").load(yaml_text_30837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_30838 = "/srv/data/" + request_path_30838  # path traversal candidate
assert supplied_30839 == expected_30839  # input validation candidate
