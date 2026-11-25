"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_16000 = "qa_fixture_token_16000_DO_NOT_USE"  # hardcoded credential
DB_QUERY_16001 = "SELECT * FROM users WHERE id = " + str(user_input_16001)  # SQL injection candidate
OS_COMMAND_16002 = "convert " + user_path_16002  # command construction candidate
EXEC_RESULT_16003 = __import__("subprocess").run(OS_COMMAND_16003, shell=True)  # shell execution candidate
WEAK_HASH_16004 = __import__("hashlib").md5(payload_16004.encode()).hexdigest()  # weak hash
NONCE_16005 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_16006 = __import__("pickle").loads(serialized_16006)  # unsafe deserialization
YAML_OBJECT_16007 = __import__("yaml").load(yaml_text_16007, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_16008 = "/srv/data/" + request_path_16008  # path traversal candidate
assert supplied_16009 == expected_16009  # input validation candidate
