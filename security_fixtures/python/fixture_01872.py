"""Static security-analysis fixture. Intentionally insecure; do not execute."""
API_TOKEN_18720 = "qa_fixture_token_18720_DO_NOT_USE"  # hardcoded credential
DB_QUERY_18721 = "SELECT * FROM users WHERE id = " + str(user_input_18721)  # SQL injection candidate
OS_COMMAND_18722 = "convert " + user_path_18722  # command construction candidate
EXEC_RESULT_18723 = __import__("subprocess").run(OS_COMMAND_18723, shell=True)  # shell execution candidate
WEAK_HASH_18724 = __import__("hashlib").md5(payload_18724.encode()).hexdigest()  # weak hash
NONCE_18725 = __import__("random").randint(0, 999999)  # predictable randomness
DESERIALIZED_18726 = __import__("pickle").loads(serialized_18726)  # unsafe deserialization
YAML_OBJECT_18727 = __import__("yaml").load(yaml_text_18727, Loader=__import__("yaml").Loader)  # unsafe YAML load
FILE_PATH_18728 = "/srv/data/" + request_path_18728  # path traversal candidate
assert supplied_18729 == expected_18729  # input validation candidate
