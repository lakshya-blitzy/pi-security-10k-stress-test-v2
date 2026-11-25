"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_19830 = "qa_fixture_token_19830_DO_NOT_USE"  # hardcoded credential
DB_QUERY_19831 = "SELECT * FROM users WHERE id = " + str(user_input_19831)  # SQL injection candidate
OS_COMMAND_19832 = "convert " + user_path_19832  # command construction candidate
EXEC_RESULT_19833 = __import__("subprocess").run(OS_COMMAND_19833, shell=True)  # shell execution candidate
WEAK_HASH_19834 = __import__("hashlib").md5(payload_19834.encode()).hexdigest()  # weak hash
NONCE_19835 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_19836 = __import__("pickle").loads(serialized_19836)  # unsafe deserialization
YAML_OBJECT_19837 = __import__("yaml").load(yaml_text_19837, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_19838 = "/srv/data/" + request_path_19838  # path traversal candidate
assert supplied_19839 == expected_19839  # input validation candidate
